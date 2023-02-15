import timeit

# Config
model_name = "EleutherAI/gpt-j-6B"

# Import Dependencies
print('Importing Dependenices...')
start = timeit.default_timer()
from transformers import AutoTokenizer, AutoModelForCausalLM, GPTJForCausalLM, pipeline
import torch
stop = timeit.default_timer()
print('\tTime: ', stop - start)

# Check GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

# Loading Tokenizer
print('Loading Tokenizer... (' + model_name +')')
start = timeit.default_timer()
tokenizer = AutoTokenizer.from_pretrained(model_name)
stop = timeit.default_timer()
print('\tTime: ', stop - start)  

# Loading Model
print('Loading Model...(' + model_name +')')
start = timeit.default_timer()
#model = AutoModelForCausalLM.from_pretrained(model_name)
model = GPTJForCausalLM.from_pretrained(
    model_name,
    revision="float16",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True
)
stop = timeit.default_timer()
print('\tTime: ', stop - start)  


def generate(text,the_model,max_length,temperature,repetition_penalty):
    generator = pipeline('text-generation', model=the_model)
    result = generator(text, num_return_sequences=3,
        max_length=max_length,
        temperature=temperature,
        repetition_penalty = repetition_penalty,
        no_repeat_ngram_size=2,early_stopping=False)
    return result[0]["generated_text"],result[1]["generated_text"],result[2]["generated_text"]

def complete_with_gpt(text,context,the_model,max_length,temperature,repetition_penalty):
    # Use the last [context] characters of the text as context
    max_length = max_length+context
    return generate(text[-context:],the_model,max_length,temperature,repetition_penalty)


print('Ready for text generation!\n')

context1 = """In a shocking finding, scientists discovered a herd of unicorns living in a remote, 
            previously unexplored valley, in the Andes Mountains. Even more surprising to the 
            researchers was the fact that the unicorns spoke perfect English."""
context2 = """Hello my name is Robin and I'm a pirate. In my last adventure I """
context3 = """Once upon a time,"""

inputs = [context1, context2, context3]

for i in inputs:
    print('Input: ' + i)
    start = timeit.default_timer()
    context = 200 # 1 - 500
    max_length = 20 # 50
    temperature = 0.9 # 1
    repetition_penalty = 1.5 # 0.2 - 2 
    res = complete_with_gpt(i, context, model_name, max_length, temperature, repetition_penalty)

    print('Response: ' + res)
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
