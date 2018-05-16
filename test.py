import sys
sys.path.append(".")

from main import *

if __name__ == '__main__':
	data = r'a:5:{i:0;a:3:{s:2:"id";s:2:"72";s:3:"img";s:67:"http://imgwx3.2345.com/h5img/upload/rotation_img/20171212100404.jpg";s:3:"url";s:38:"http://h5.2345.com/default/GameDetail/";}i:1;a:3:{s:2:"id";s:2:"71";s:3:"img";s:67:"http://imgwx2.2345.com/h5img/upload/rotation_img/20171130152956.gif";s:3:"url";s:18:"http://h5.2345.com";}i:2;a:3:{s:2:"id";s:2:"73";s:3:"img";s:67:"http://imgwx4.2345.com/h5img/upload/rotation_img/20171212100447.jpg";s:3:"url";s:38:"http://h5.2345.com/default/GameDetail/";}i:3;a:3:{s:2:"id";s:2:"65";s:3:"img";s:67:"http://imgwx1.2345.com/h5img/upload/rotation_img/20171018154912.gif";s:3:"url";s:38:"http://h5.2345.com/default/GameDetail/";}i:4;a:3:{s:2:"id";s:2:"58";s:3:"img";s:67:"http://imgwx4.2345.com/h5img/upload/rotation_img/20180205152128.jpg";s:3:"url";s:3:"123";}}'
	lex = Lexer(data)
	ret = lex.parse()
	print(ret)