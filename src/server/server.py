import json
from operator import sub

import aioconsole
from error_thrower import Error_Objective
import fastapi
from Game import Game
from fastapi import FastAPI, WebSocket
from submission import Submission

error_obj = Error_Objective()


game = Game()
app = FastAPI()
clients: dict[str, WebSocket] = {}


async def register_user(username: str, websocket: WebSocket):
    """Registers a user with the server if the username is not already taken"""
    if username not in clients.keys():
        await game.login(username)
        clients[username] = websocket
    else:
        await websocket.send_json({'type': 'error', 'error': "Username already taken"})
        await websocket.close()


async def get_leaderboard(websocket: WebSocket):
    """Returns the leaderboard"""
    await websocket.send_json({'type': 'text', 'text': await game.get_leaderboard()})
    
async def test(websocket: WebSocket, code: str, error: str):
    s = Submission(code)
    await websocket.send_json({'type': 'text', 'text': 'Your code raised the error provided!' if (await s.hit_target(error))[1] else 'Your code did not raise the error provided, try testing again'})
    del s
    
async def submit(websocket: WebSocket, code: str, user: str):
    submission = Submission(code)
    await game.submit(user, code)     
    await websocket.send_json({'type': 'text', 'text': 'Your code raised the error provided!' if (await submission.hit_target(code))[1] else 'Your code did not raise the error provided.'})
    del submission


@app.websocket("/")
async def root(websocket: WebSocket):
    """This function is called when a websocket connection is made to http://localhost:8000/"""
    try:
        await websocket.accept()
        
        data = await websocket.receive_json()
        
        match data['type']:
            case "register":
                user = data['data']
                await register_user(user, websocket)
                await websocket.send_json({f'type': 'text', 'text': f'Logged in as {user}!'})
                print(f'{user} joined the game.')
                
            case _:
                await websocket.send_json({'type': 'error', 'error': 'Register user first.'})
                await websocket.close()

        while True:
            
            error = error_obj.objective()
            await game.new_target(user, error)   
            while True:
                await websocket.send_json({'type': 'text', 'text': f'Produce error {error}.'})
                data = await websocket.receive_json()
                match data['type']:
                    case "leaderboard":
                        await get_leaderboard(websocket)
                        
                    case "test":
                        await test(websocket, data['data'])
                        
                    case "submission":
                        await submit(websocket, data['data'], user)
                        break
                    
                    case 'logout':
                        await websocket.close()
                        
                    case _ as err:
                        print(f'Unsupported request type - {err}')
                        
    except fastapi.WebSocketDisconnect:
        try:
            await game.logout(user)
            del clients[user]
            print(f'{user} left the game')
        except UnboundLocalError:
            pass
        
    
            
