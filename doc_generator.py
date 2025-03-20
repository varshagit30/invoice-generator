from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")

invoice_list = [[2,"pen", 10, 20]]

doc.render({"name": "john", "invoice_list": invoice_list})
doc.save("new_invoice.docx")
