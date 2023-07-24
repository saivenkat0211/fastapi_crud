from fastapi import FastAPI
app = FastAPI()

#base route of the app
@app.get("/",tags = ['ROOT'])
async def root() -> dict:
    return {"ping":"pong"}

#get - to read
@app.get('/todo',tags = ['todos'])
async def get_doto()->dict:
    return{"data":todos}


todos = [
    {
        "id":"1",
        "activity": "namasthe"
    },
    {
        "id":"2",
        "activity":"vanakkam"
    }

]

#post - to create
@app.post('/something',tags = ["todos"])
async def add_todo(todo:dict)->dict:
    todos.append(todo)
    return {
        "data":"todo has been added"
    }
    
#put - to update 


@app.put('/todo/{id}',tags = ['todos'])
async def update_todo(id:int,body:dict) ->dict:
    for x in todos:
        # print(x["id"])
        if (int(x["id"])) == id:
            x['activity'] = body['activity']
            return {
                'data': f"updated the {id}"
            } 
    return {"body":"nothing to be updated"}
#delete - to delete

@app.delete('/todo/{id}',tags = ["todos"])
async def delete_todo(id:int)->dict:
    for x in todos:
        if int(x["id"]) == id:
            todos.remove(x)
            return {
                "data":f"{id} deleted"
            }
    return {
        "data":f"{id} cant be deleted"
    }
