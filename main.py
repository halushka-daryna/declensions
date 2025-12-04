import stanza
import gradio as gr
from analyzer.declensions import analyze_text
from analyzer.utils import parse_feats

stanza.download("uk")
nlp = stanza.Pipeline("uk")

TEST_SENTENCES = [
    "В кіно представили нову колекцію, а ягня мирно паслося поруч у полі.",
    "Вчора мати купила хліб та відвезла його на таксі до бабусі.",
    "Після дощу земля була мокрою, а дітям роздали цукерки."
]

def test_sentence(index):
    text = TEST_SENTENCES[index]
    doc = nlp(text)
    return text, analyze_text(doc)

with gr.Blocks() as demo:
    gr.Markdown("## Визначення відмін іменників")
    text_input = gr.Textbox(lines=5, label="Введіть ваш текст")
    output_table = gr.Dataframe(headers=["Слово", "Лема", "Рід", "Відміна"], label="Результати обробки")
    
    with gr.Row():
        analyze_btn = gr.Button("Аналізувати текст")
        test1_btn = gr.Button("Тест 1")
        test2_btn = gr.Button("Тест 2")
        test3_btn = gr.Button("Тест 3")
    
    analyze_btn.click(fn=lambda text: analyze_text(nlp(text)), inputs=text_input, outputs=output_table)
    test1_btn.click(fn=lambda: test_sentence(0), inputs=None, outputs=[text_input, output_table])
    test2_btn.click(fn=lambda: test_sentence(1), inputs=None, outputs=[text_input, output_table])
    test3_btn.click(fn=lambda: test_sentence(2), inputs=None, outputs=[text_input, output_table])

demo.launch()
