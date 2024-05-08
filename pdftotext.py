# # import pdfplumber
# # import pytesseract
# # import re
# # from PIL import Image

# # # Function to extract text within a bounding box (x0, y0, x1, y1)
# # def extract_text_within_bbox(page, bbox):
# #     cropped_page = page.within_bbox(bbox)
# #     text = cropped_page.extract_text()
    
# #     # If no text is found, use pytesseract to extract it
# #     if not text:
# #         image = cropped_page.to_image(resolution=300)
# #         text = pytesseract.image_to_string(image.image)

# #     return text

# # # Function to join lines based on specific conditions
# # def join_lines(text):
# #     lines = text.split("\n")
# #     new_lines = []
# #     for i in range(len(lines)):
# #         if i > 0 and (lines[i].startswith('(') or lines[i][0].islower()):
# #             new_lines[-1] = new_lines[-1].strip() + ' ' + lines[i]
# #         elif i < len(lines) - 1 and (lines[i].endswith(',') or lines[i][-1].isdigit()):
# #             lines[i+1] = lines[i] + ' ' + lines[i+1]
# #         else:
# #             new_lines.append(lines[i])
# #     return "\n".join(new_lines)

# # # Function to split text into subgroups based on a regex pattern
# # def split_into_subgroups(text):
# #     text = join_lines(text)
# #     new_text = text.split("\n")
# #     subgroups = []
# #     counter = -1
# #     pattern = r'^(ECP|Avantaguard|Appearance|Protection)'

# #     for line in new_text:
# #         if re.match(pattern, line):
# #             subgroups.append("")
# #             counter += 1
# #         if counter >= 0:  # Ensure there's at least one subgroup
# #             subgroups[counter] += line + "\n"

# #     return [group.strip() for group in subgroups if group.strip()]

# # def remove_empty_strings(string_list):
# #     return list(filter(None, string_list))

# # # Open the PDF and read the first page
# # with pdfplumber.open('try.pdf') as pdf:
# #     first_page = pdf.pages[0]
    
# #     # Define bounding boxes for each section
# #     name_bbox = (148, 23, 333, 38)
# #     model_bbox = (148, 37, 332, 59)
# #     premium_bbox = (28, 75, 268, 513)
# #     preferred_bbox = (276, 75, 516, 513)
# #     essential_bbox = (523, 75, 763, 513)
# #     premium_price_bbox = (28, 513, 270, 528)
# #     preferred_price_bbox = (276, 513, 516, 528)
# #     essential_price_bbox = (523, 513, 763, 528)
    
# #     # Extract text under each section using the defined bounding boxes also name and model
# #     name_text = extract_text_within_bbox(first_page, name_bbox)
# #     model_text = extract_text_within_bbox(first_page, model_bbox)
# #     premium_text = extract_text_within_bbox(first_page, premium_bbox)
# #     preferred_text = extract_text_within_bbox(first_page, preferred_bbox)
# #     essential_text = extract_text_within_bbox(first_page, essential_bbox)
# #     premium_price_text = extract_text_within_bbox(first_page, premium_price_bbox)
# #     preferred_price_text = extract_text_within_bbox(first_page, preferred_price_bbox)
# #     essential_price_text = extract_text_within_bbox(first_page, essential_price_bbox)

# # # Now you can call split_into_subgroups without needing to pass patterns or key_terms
# # premium_subgroups = remove_empty_strings(split_into_subgroups(premium_text))
# # preferred_subgroups = remove_empty_strings(split_into_subgroups(preferred_text))
# # essential_subgroups = remove_empty_strings(split_into_subgroups(essential_text))

# # # Output the extracted information along with their respective sub-groups
# # print("\nCustomer Name: ")
# # print(name_text)
# # print("\nCar Model: ")
# # print(model_text)

# # # Output the subgroups for each section
# # print("\nPremium Services Subgroups:")
# # for subgroup in premium_subgroups:
# #     print(subgroup)
# #     print("NEXT")

# # print("\nPreferred Services Subgroups:")
# # for subgroup in preferred_subgroups:
# #     print(subgroup)
# #     print("NEXT")

# # print("\nEssential Services Subgroups:")
# # for subgroup in essential_subgroups:
# #     print(subgroup)
# #     print("NEXT")

# # print("\nPremium Price:")
# # print(premium_price_text)
# # print("\nPreferred Price:")
# # print(preferred_price_text)
# # print("\nEssential Price:")
# # print(essential_price_text)



# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #
# #                                       CURRENT CODE
# #
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import pdfplumber
# # import pytesseract
# import re
# from PIL import Image

# # Function to extract text within a bounding box (x0, y0, x1, y1)
# def extract_text_within_bbox(page, bbox):
#     cropped_page = page.within_bbox(bbox)
#     text = cropped_page.extract_text()
    
#     # If no text is found, use pytesseract to extract it
#     if not text:
#         image = cropped_page.to_image(resolution=300)
#         text = pytesseract.image_to_string(image.image)

#     return text

# # Function to join lines based on specific conditions
# def join_lines(text):
#     lines = text.split("\n")
#     new_lines = []
#     for i in range(len(lines)):
#         if i > 0 and (lines[i].startswith('(') or lines[i][0].islower()):
#             new_lines[-1] = new_lines[-1].strip() + ' ' + lines[i]
#         elif i < len(lines) - 1 and (lines[i].endswith(',') or lines[i][-1].isdigit()):
#             lines[i+1] = lines[i] + ' ' + lines[i+1]
#         else:
#             new_lines.append(lines[i])
#     return "\n".join(new_lines)

# # adds dashes before an element in list gets indented
# def add_dashes(sample_list):
#     new_list = []
#     for element in sample_list:
#         new_list.append( element.replace("\n", "\n- "))
#     return new_list 
    

# # Function to split text into subgroups based on a regex pattern
# def split_into_subgroups(text):
#     text = join_lines(text)
#     new_text = text.split("\n")
#     subgroups = []
#     counter = -1
#     pattern = r'^(ECP|Avantaguard|Appearance|Protection)'

#     for line in new_text:
#         if re.match(pattern, line):
#             subgroups.append("")
#             counter += 1
#         if counter >= 0:  # Ensure there's at least one subgroup
#             subgroups[counter] += line + "\n"

#     return [group.strip() for group in subgroups if group.strip()]

# # Removes empty strings from the text
# def remove_empty_strings(string_list):
#     return list(filter(None, string_list))

# # Converts the text(s) to a list
# def text_to_list(*args):
#     res = []
#     for arg in args:
#         res.append(arg)
#     return res

# # Open the PDF and read the first page
# with pdfplumber.open(file) as pdf:
#     first_page = pdf.pages[0]
    
#     # Define bounding boxes for each section
#     name_bbox = (148, 23, 333, 38)
#     model_bbox = (148, 37, 332, 59)
#     premium_bbox = (28, 75, 268, 513)
#     preferred_bbox = (276, 75, 516, 513)
#     essential_bbox = (523, 75, 763, 513)
#     premium_price_bbox = (28, 513, 270, 528)
#     preferred_price_bbox = (276, 513, 516, 528)
#     essential_price_bbox = (523, 513, 763, 528)
    
#     # Extract text under each section using the defined bounding boxes also name and model
#     name_text = extract_text_within_bbox(first_page, name_bbox)
#     model_text = extract_text_within_bbox(first_page, model_bbox)
#     premium_text = extract_text_within_bbox(first_page, premium_bbox)
#     preferred_text = extract_text_within_bbox(first_page, preferred_bbox)
#     essential_text = extract_text_within_bbox(first_page, essential_bbox)
#     premium_price_text = extract_text_within_bbox(first_page, premium_price_bbox)
#     preferred_price_text = extract_text_within_bbox(first_page, preferred_price_bbox)
#     essential_price_text = extract_text_within_bbox(first_page, essential_price_bbox)

# # Split extracted texts into subgroups using key terms
# premium_list = add_dashes(remove_empty_strings(split_into_subgroups(premium_text)))
# preferred_list = add_dashes(remove_empty_strings(split_into_subgroups(preferred_text)))
# essential_list = add_dashes(remove_empty_strings(split_into_subgroups(essential_text)))

# client_list = text_to_list(name_text)
# print(client_list)
# print()

# vehicle_list = text_to_list(model_text)
# print(vehicle_list)
# print()

# finance_list = text_to_list("")

# biweekly_list = text_to_list(premium_price_text, preferred_price_text, essential_price_text)

# client_wishes_take_list = []

# client_info_dict = {"Client": client_list, 
#                     "Vehicle": vehicle_list, 
#                     "Financial Information": finance_list}
# preferrence_info_dict = {"Premium": premium_list,
#                         "Preferred": preferred_list,
#                         "Essential": essential_list}

# payment_info_dict = {"Biweekly Payment": biweekly_list, 
#                     "Client wishes to take": client_wishes_take_list}
    
