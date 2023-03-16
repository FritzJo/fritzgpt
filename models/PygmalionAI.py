from transformers import AutoTokenizer, AutoModelForCausalLM
import timeit


def load_model(target_model_name):
    # Loading Tokenizer
    print("[INFO] Loading Tokenizer...(" + target_model_name + ")")
    start = timeit.default_timer()
    chat_tokenizer = AutoTokenizer.from_pretrained(target_model_name)
    stop = timeit.default_timer()
    print('--> Done in ', stop - start)

    # Loading Model
    print("[INFO] Loading Model... (" + target_model_name + ")")
    start = timeit.default_timer()
    chat_model = AutoModelForCausalLM.from_pretrained(target_model_name).to("cuda")
    stop = timeit.default_timer()
    print('--> Done in ', stop - start)
    return chat_model, chat_tokenizer, ["You", "FritzGPT"]


def build_prompt(history):
    history.append("FritzGPT: ")
    return "\n".join(history)


def chat(history):
    prompt = build_prompt(history)
    output = generate_response(prompt)
    cleaned_output = output.replace(prompt, "").split("You:")[0].replace("\n\n", "\n")
    return cleaned_output


def generate_response(instruction):
    input_ids = tokenizer(instruction, return_tensors="pt").input_ids.to("cuda")
    gen_tokens = model.generate(input_ids,
                                do_sample=True,
                                temperature=0.9,
                                max_new_tokens=50,
                                top_p=0.9)
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    return gen_text


model_name = "PygmalionAI/pygmalion-2.7b"
model, tokenizer, interlocutor_names = load_model(model_name)
