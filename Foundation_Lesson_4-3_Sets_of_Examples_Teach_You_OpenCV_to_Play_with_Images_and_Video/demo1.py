# 导入opencv 
import cv2
# 读取
img = cv2.imread('./img/cat.jpg')

# 单独用这个会快速显示并关闭
# cv2.imshow('display image',img)

while True:
    # 不停的显示
    cv2.imshow('display image',img)

    # 如果等待至少1ms ，而且按了ESC 键，也可以用 ord('q')
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 关闭所有窗口
cv2.destroyAllWindows()