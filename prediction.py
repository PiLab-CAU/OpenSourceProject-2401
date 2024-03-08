from openai import OpenAI


class openai_stock_prediction:
  def __init__(self):

    self.client = OpenAI(api_key='put_your_api_key')
    self.base_prompt = "Economic Self-Reliance Is a Dangerous Delusion: negative\
              \nWall St climbs, powered by chips, megacaps earning in focus: positve\
              \nUS consumer sentiment rises solidly in January: positive\
              \nUS equity funds see big outflows on rate-cut uncertainty, earnings caution: negative\
              \ngiven the two example, complete the below sentence with positve or negative."
    self.max_qeury_len = 100
    
  def renew_prompt(self):
     return self.base_prompt

  def update_prompt(self, base_prompt, prompt):
     return base_prompt+'\n'+prompt
  
  def health_checker(self, text, max_len=30000):
        if len(text) > max_len:
            return text[:max_len]
        else:
            return text
  
  def predict(self, user_question, queries):
    if len(queries) > self.max_qeury_len:
       queries = queries[:self.max_qeury_len]

    prompt = self.base_prompt
    for query_set in queries:
       query = query_set[1]
       print("updating prompt: {}".format(query))
       prompt = self.update_prompt(prompt, query)
    
    print("prompt to be used:\n{}".format(prompt))

    completion = self.client.chat.completions.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_question}
      ]
    )
    return completion.choices[0].message.content



if __name__ == "__main__":
  print('prediction')