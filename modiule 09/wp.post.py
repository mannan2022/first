import wp_func
first_pragraphs_text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
heading_one_text='Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old'
second_pragraphs_text="t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout"
atricle=wp_func.wp_pragraphs(first_pragraphs_text)+wp_func.wp_h2(heading_one_text)+wp_func.wp_pragraphs(second_pragraphs_text)
print(atricle)
import wp_func
# first_pragraphs="Lorem Ipsum is simply dummy text of the printing and typesetting industry"
# heading_one="Contrary to popular belief, Lorem Ipsum is not simply random text"
# two="is a long established fact that a reader will be distracted"
# var=wp_func.wp_para(first_pragraphs)+wp_func.h2(heading_one)+wp_func.wp_para(two)
# print(var)
