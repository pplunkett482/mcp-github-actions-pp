# predict.py
# written by ChatGPT

def predict(input_text):
    return f"Echo: {input_text}"

if __name__ == "__main__":
    import sys
    print(predict(sys.argv[1]))
