print('Importing Dependenices...')
import timeit
from transformers import AutoTokenizer, AutoModelForCausalLM, GPTJForCausalLM, pipeline, GPT2Tokenizer, GPT2Model, \
    AutoModelForSeq2SeqLM
import torch

# Config
# model_name = "EleutherAI/gpt-j-6B"
# model_name = "gpt2-medium"
# model_name = "facebook/opt-66b"
model_name = "microsoft/GODEL-v1_1-large-seq2seq"

# Check GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)

# Loading Tokenizer
print('Loading Tokenizer... (' + model_name + ')')
start = timeit.default_timer()
tokenizer = AutoTokenizer.from_pretrained(model_name)
stop = timeit.default_timer()
print('\tTime: ', stop - start)

# Loading Model
print('Loading Model...(' + model_name + ')')
start = timeit.default_timer()
# model = AutoModelForCausalLM.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name
    # torch_dtype=torch.float16,
    # revision="float16",
    # low_cpu_mem_usage=True,
    # device_map='auto',
    # load_in_8bit=True
)
stop = timeit.default_timer()
print('\tTime: ', stop - start)


def generate(text, the_model, max_length, temperature, repetition_penalty):
    generator = pipeline('text-generation', model=the_model)
    result = generator(text, num_return_sequences=3,
                       max_length=max_length,
                       temperature=temperature,
                       repetition_penalty=repetition_penalty,
                       no_repeat_ngram_size=2, early_stopping=False)
    return result[0]["generated_text"]


def generateChat(instruction, knowledge, dialog):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output


print('Ready for text generation!\n')

context1 = """In a shocking finding, scientists discovered a herd of unicorns living in a remote,
            previously unexplored valley, in the Andes Mountains. Even more surprising to the
            researchers was the fact that the unicorns spoke perfect English."""
context2 = """Hello my name is Robin and I'm a pirate. In my last adventure I """
context3 = """Once upon a time,"""
context4 = """You are a conversational language model created by OpenAI. Your name is FritzGPT and you answer a users questions. This is the current conversation.
Q: Hi. Whats your name?
A: """

inputs = []

for i in inputs:
    print('--Input: ' + i)
    start = timeit.default_timer()
    res = generate(i, the_model=model_name, max_length=len(i) + 200, temperature=0.9, repetition_penalty=1.5)

    print('--Response:')
    print(res)
    stop = timeit.default_timer()
    print('--Time: ', stop - start)

instruction = f'Instruction: given a dialog context, you need to response empathically.'
knowledge = ''
dialog = [
    'Does money buy happiness?',
    'It is a question. Money buys you a lot of things, but not enough to buy happiness.',
    'What is the best way to buy happiness ?'
]
response = generateChat(instruction, knowledge, dialog)
print(response)
