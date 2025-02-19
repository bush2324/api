from fastapi import FastAPI
from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from pydantic import BaseModel

# 登錄 Hugging Face Token
login(token="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")  # 替換為你的 Token

# 定義工具和模型
search_tool = DuckDuckGoSearchTool()
model = HfApiModel()
agent = CodeAgent(tools=[search_tool], model=model)

# 初始化 FastAPI 應用
app = FastAPI()

# 定義一個路由來處理查詢請求
@app.get("/query")
async def query(question: str):
    result = agent.run(question)
    return {"question": question, "answer": result}

@app.get("/query")
async def query(question: str):
    result = agent.run(question)
    return {"question": question, "answer": result}
# 定義根路徑的處理器（選擇性）
@app.get("/")
async def read_root():
    return {"message": "~葉家豪熊"}

responses = {
    "葉家豪": "超雄聖體",
    "溫維智": "旗津第一長髮男"
}

class InputName(BaseModel):
    name: str

@app.get("/api/測試")
async def test_api(name: str):
    # 根據名稱返回對應的結果，若找不到則返回錯誤訊息
    response = responses.get(name, "未知的人物")
    return {"input": name, "output": response}

@app.get("/api/測試")
async def test_api(name: str):
    # 根據名稱返回對應的結果，若找不到則返回錯誤訊息
    response = responses.get(name, "未知的人物")
    return {"input": name, "output": response}


# 啟動 FastAPI 服務器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=1234, reload=True)
