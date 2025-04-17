import spacy

# 加载英文模型
nlp = spacy.load("en_core_web_sm")


def analyze_sentence(sentence):
    doc = nlp(sentence)
    print(f"\n🔍 句子分析: {sentence}")
    print("------------------------------------------------")

    # 打印词性和依存关系
    for token in doc:
        print(f"{token.text:<12} | {token.pos_:<10} | {token.dep_:<12} | head: {token.head.text}")

    # 函数结构输出
    print("\n📦 函数结构化表示（动词作为函数调用）：")
    for token in doc:
        if token.pos_ == "VERB":
            verb = token.text
            subject = [t.text for t in token.children if t.dep_ in ("nsubj", "nsubjpass")]
            obj = [t.text for t in token.children if t.dep_ in ("dobj", "obj")]
            print(f"{verb}(")
            print(f"  subject = {', '.join(subject) or 'None'},")
            print(f"  object  = {', '.join(obj) or 'None'}")
            print(")")
