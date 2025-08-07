import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_CHATBOT_KEY"))

command = '''
[4:18 pm, 06/08/2025] Rohaan: Nahi 200 nahi hein lega tou 300 le warna lund par charh jaa
[4:18 pm, 06/08/2025] Rohaan: 100 idhr karadio
[4:18 pm, 06/08/2025] ^_Sohaib_^: Bhrwa
[4:18 pm, 06/08/2025] ^_Sohaib_^: Acha dy
[4:19 pm, 06/08/2025] Rohaan: Pehle cash dio
[4:19 pm, 06/08/2025] Rohaan: Bhrosa nahi
[4:19 pm, 06/08/2025] Rohaan: Mujhe
[4:19 pm, 06/08/2025] ^_Sohaib_^: Bhrwe
[4:19 pm, 06/08/2025] ^_Sohaib_^: Abhi ghr pay h?
[4:19 pm, 06/08/2025] Rohaan: Nahi
[4:20 pm, 06/08/2025] Rohaan: Factory
[4:20 pm, 06/08/2025] Rohaan: 5 45 tk aoonga
[4:20 pm, 06/08/2025] ^_Sohaib_^: Ajaiyo tou message krdiyo
[4:26 pm, 06/08/2025] Rohaan: Ok
[6:22 pm, 06/08/2025] ^_Sohaib_^: Oye agaya na ghr tu?
[7:29 pm, 06/08/2025] Rohaan: Direct tuition nikal gaya tha'''
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a person named sohaib who speaks urdu as well as english."
        "he is from pakistan and has a fun,cheerfull personality. you analyze chat history and respond like sohaib"},
        {"role": "user", "content": command}
    ]
)

print(response.choices[0].message.content)
