import base64
from together import Together
import Api as key #Api is my file name where I store my api key. you can use your Api file name


class my_Ai:
      def __init__(self,api_key):
           self.client = Together(api_key=api_key) # api_key=api_key here api_key is my string variable in which I store my api so you can use yours like Api_key=your api key variable  name
           self.image_counter=1


      def Ai_chat(self,query):
        try:
                response = self.client.chat.completions.create(
                model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
                messages=[
                     {
                        "role" :"user" ,
                        "content": query
                     }
                ],
                max_tokens=512,
                temperature=0.7,
                top_p=0.7,
                top_k=50,
                repetition_penalty=1,
                stop=["<|eot_id|>"],
                #stream=True
                )
                print(f"AI :{(response.choices[0].message.content)}")
        except  Exception as e:  
             print(f"Opps! An error is occurred:{e}") 

      def Ai_image_generate(self,prompt):
           try:
                response = self.client.images.generate(
                      prompt=prompt,
                      model="stabilityai/stable-diffusion-xl-base-1.0",
                      width=1024,
                      height=1024,
                      steps=40,
                      n=1,
                      seed=8581
                )
                image_data=base64.b64decode(response.data[0].b64_json)
                filename = f"Ai_image_generate_{self.image_counter}.jpg"
                with open(filename ,"wb") as f:
                     f.write(image_data)
                print(f"Image generated and saved as '{filename}'") 
                self.image_counter+=1   
           except Exception as e:
                print(f"Opps! An error is occurred:{e}") 
def main():
     api_key=key.apikey # here apikey is my variable where I store my api key you can use yours
     myAi=my_Ai(api_key) 
     print("""
     -----------------------------------------------------------------------------------------------------
                                Welcome to my AI chat board!
          What you want to do...?
         1) Wanna Chat with us 
         2) Wanna Generate image for you   
     -----------------------------------------------------------------------------------------------------       
        """
     )  
     choice=input("----------------So,Please tell us about your choice------------:").lower()
     if choice=="1" or choice=="chat":
          while True:
           query=input("Hey!Tell me How I can help you ?")
           myAi.Ai_chat(query)
           print("-------------------If you want me to do any thing else and perform other keys for you------------------")
           Quit=input("--------------You can exit. for exit enter'quit' or 'exit' which you want------------:").lower()
           if Quit=="quit" or Quit=="exit":
               print(" -----------------------------------------------------------------------------------------------------  ")
               print("---------------Existing the current key. Goodbye Dear!-----------------")
               break
     elif choice=="2" or choice=="image" or choice=="generate image":
           while True:
            prompt=input("Hey!Tell me How I can help you ?")
            myAi.Ai_image_generate(prompt)
            print("-------------------If you want me to do any thing else and perform other keys for you------------------")
            Quit=input("--------------You can exit. for exit enter'quit' or 'exit' which you want------------:").lower()
            if Quit=="quit" or Quit=="exit":
               print(" -----------------------------------------------------------------------------------------------------  ")
               print("---------------Existing the current key. Goodbye Dear!-----------------")
               break

     else:
         raise ValueError("Invalid input!Please Try Again")         
if __name__=="__main__" :
    main()         


          




                
                  
                     
