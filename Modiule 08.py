# def add(x):
#     result=x**2+x*2+6
#     return result
# print(add(3))
# print(add(20))
# def singelvariable(X):
#     result=X**5+X*5+50
#     return result
# print(singelvariable(6))
# print(singelvariable(25))
# def number(y):
#     output=y**6+y*6+30
#     return output
# print(number(16))
# def add (x,y,z):
#     result=x+y+z
#     return result
# print(add(2,3,5))
# def slugify(text):
#     slug=text.strip().lower().replace(' ','-')
#     return slug
# title=input('Enter Your Title:')
# slug=slugify(title)
# print(slug)
# def add(x):
#     number=x**3+x*5+25
#     return number
# print(add(3))
# def singel(y):
#     result=y**5+y*3+21
#     return result
# print(singel(15))
# def heading_two(text,html_tag):
#     """
#     Return HTML Tag for any text
#     :param text:
#     :param html tag:what kind of tag you want genarate
#     :return:
#     """
#     html=f'<{html_tag}>{text}</{html_tag}>'
#     return html
# print(heading_two.__doc__)
# def html_tag(text,html):
#     """
#     thhis is html tag
#     peramiter: what kind of perameter you wan genarte
#     return: any kind of html text"""
#     html=f'<{html}>{text}</{html}>'
#     return html
# print(html_tag.__doc__)
# # def paragraphs(text,html_tag):
# #     result=f'<{html_tag}>{text}</{html_tag}>'
# #     return result
# # print(paragraphs('This is paragrpahs','h6'))
# def css(text,html):
#     """
#     This is html tag
#     para:You can genarte any kind of html tag
#     return: any kind of html tag
#     """
#     book=f'<{html}>{text}</{html}>'
#     return book
# print(css.__doc__)
# def java(num,html_tag):
#     name=f'<{html_tag}{num}</{html_tag}>'
#     return name
# print(java('This is a paragraphs','p'))
def tringle(base,height):
    area=0.5*base*height
    return area
def sqaure(length):
    area=length*length
    return area
def rectangle(length,width):
    area=length*width
    return area
print(rectangle(5,6))

