from transformers import AutoTokenizer, AutoModelForCausalLM, GPTJForCausalLM, pipeline, GPT2Tokenizer, GPT2Model, \
    AutoModelForSeq2SeqLM
import torch
import timeit

from output import print_custom

model_name = "PygmalionAI/pygmalion-2.7b"

# Loading Tokenizer
print_custom("warn", "[INFO] Loading Tokenizer...(" + model_name + ")")
start = timeit.default_timer()
tokenizer = AutoTokenizer.from_pretrained(model_name)
stop = timeit.default_timer()
print('--> Done in ', stop - start)

# Loading Model
print_custom("warn", "[INFO] Loading Model... (" + model_name + ")")
start = timeit.default_timer()
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")

interlocutor_names = ["You", "FritzGPT"]


def build_prompt(history):
    history.append("FritzGPT: ")
    return "\n".join(history)


def chat(history):
    prompt = build_prompt(history)
    output = generateChat(prompt)
    print("OUTPUT")
    print(output)
    print("-------------------------\nCLEANED")
    # print(output.replace(prompt, ""))
    # print("-------------------------")
    cleaned_output = output.replace(prompt, "").split("You:")[0].replace("\n\n", "\n")
    return cleaned_output


def clean_chat_output(txt, prompt):
    delimiter = "\n" + interlocutor_names[0]
    output = txt.replace(prompt, '')
    output = output[:output.find(delimiter)]
    return output


def generateChat(instruction):
    input_ids = tokenizer(instruction, return_tensors="pt").input_ids.to("cuda")
    gen_tokens = model.generate(input_ids,
                                do_sample=True,
                                temperature=0.9,
                                max_new_tokens=50,
                                top_p=0.9)
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    return gen_text
