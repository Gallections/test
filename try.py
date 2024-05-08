# from docx import Document
# import pandas as pd

# def fill_invitation(template_path, output_path, data):
#     doc = Document(template_path)

#     for paragraph in doc.paragraphs:
#         for key, value in data.items():
#             if key in paragraph.text:
#                 for run in paragraph.runs:
#                     run.text = run.text.replace(key, value)

#     doc.save(output_path)


# def generate_invitation_from_csv():
#     df = pd.read_csv("contacts.csv")
#     for idx, row in df.iterrows():
#         data = {

#         }
#         output_path = f'invitation_{idx + 1}.dox'
#         fill_invitation(template_path, output_path, data)

# if __name__ == '__main__':
    

#     csv_path = 'contacts.csv'
#     template_path = "template.docx"
#     generate_invitation_from_csv(csv_path, template_path)