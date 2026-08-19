import pandas as pd
import ollama
import json

def extract_insights(review_text):
    # We define a strict prompt to force the AI to return ONLY JSON
    prompt = f"""
    Analyze the following customer review. Extract the key aspects discussed and the sentiment (Positive, Negative, or Neutral) for each aspect.
    Respond ONLY with a valid JSON object in this exact format: {{"aspects": {{"aspect_name": "sentiment"}}}}
    
    Review: "{review_text}"
    """
    
    try:
        # We are using qwen2:1.5b here to ensure it runs fast without memory errors
        response = ollama.chat(model='qwen2:1.5b', messages=[
            {
                'role': 'system',
                'content': 'You are a highly accurate data extraction API. You output only raw, valid JSON.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ])
        
        # Parse the JSON string returned by the model into a Python dictionary
        result = json.loads(response['message']['content'])
        return result
    except Exception as e:
        print(f"Error processing review: {e}")
        return {"aspects": {}}

# 1. Load our dummy data
print("Loading reviews...")
df = pd.read_csv('amazon_raw_reviews.csv')

# We use a standard Python list to collect the processed results dynamically
processed_data_list = []

print("Starting AI NLP processing...")
# 2. Iterate through the reviews
# 2. Iterate through the reviews
for index, row in df.iterrows():
    print(f"Processing review {index + 1}/{len(df)}...")
    
    # UPDATE 1: Use the correct column name 'reviews.text'
    insights = extract_insights(row['reviews.text']) 
    
    # 3. Combine original data with AI insights
    processed_data_list.append({
        # UPDATE 2: Use the correct column name 'reviews.text'
        'original_text': row['reviews.text'],
        
        # UPDATE 3: Use the correct column name 'reviews.rating'
        'rating': row['reviews.rating'], 
        
        'extracted_aspects': json.dumps(insights.get('aspects', {}))
    })

# 4. Save the final structured data
final_df = pd.DataFrame(processed_data_list)
final_df.to_csv('processed_ai_insights.csv', index=False)
print("Pipeline complete! Check processed_ai_insights.csv")

# 2. Iterate through the reviews
for index, row in df.iterrows():
    print(f"Processing review {index + 1}/{len(df)}...")
    
    # UPDATE 1: Change 'review_text' to 'reviews.text'
    insights = extract_insights(row['reviews.text']) 
    
    # 3. Combine original data with AI insights
    processed_data_list.append({
        # UPDATE 2: Change 'review_text' to 'reviews.text'
        'original_text': row['reviews.text'],
        
        # UPDATE 3: Change 'rating' to 'reviews.rating'
        'rating': row['reviews.rating'], 
        
        'extracted_aspects': json.dumps(insights.get('aspects', {}))
    })

# 4. Save the final structured data
final_df = pd.DataFrame(processed_data_list)
final_df.to_csv('processed_ai_insights.csv', index=False)
print("Pipeline complete! Check processed_ai_insights.csv")