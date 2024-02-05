"""
演示Demo
"""

from argparse import ArgumentParser




# 参数
parser = ArgumentParser()
                     
parser.add_argument("--width", type=int, default=960,
                    help="宽度")   
parser.add_argument("--height", type=int, default=720,
                    help="高度")                           
args = parser.parse_args()

area = int (args.width * args.height)

print('面积为' + str(area) )