import uvicorn

if __name__ == '__main__':
    uvicorn.run('app.main:app', workers=1, host='0.0.0.0', port=8000
                )