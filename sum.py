from openai import OpenAI

openai.api_key = OPENAI_KEY
client = OpenAI()

def sumGPT(texts, sources):
    messag=[{"role": "system", "content": "You are a chatbot"}]
    
    ## build a chat history: you can CONDITION the bot on the style of replies you want to see - also getting weird behaviors... such as KanyeGPT
    history_bot = ["Yes, I'm ready! Please provide the articles."]
    
    # ask ChatGPT to return STRUCTURED, parsable answers that you can extract easily - often better providing examples of desired behavior (1-2 example often enough)
    history_user = ["i'll give you several articles in different languages about the same topic. The information differs slightly so you will have to a) summarize the main points that the articles agree on and most importantly b) outline the differences.\nReady to start?"]
    
    for user_message, bot_message in zip(history_user, history_bot):
            messag.append({"role": "user", "content": str(user_message)})
            messag.append({"role": "system", "content": str(bot_message)})
    cnt = 1 
    for text, source in zip(texts, sources):
        messag.append({"role": "user", "content": "Article "+ str(cnt)+ " from "+source +": "+text})
        cnt+=1

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messag)
    result = ''
    for choice in response.choices:
        result += choice.message.content
    history_bot.append(result)
    return result

sumGPT(texts, sources)
