class Token:
	def __init__(self, type, value = None):
		self.type = type
		self.value = value

	def __str__(self):
		return "%s : %s" % (self.type, self.value)

	__descr__ = __str__

class Lexer:
	def __init__(self, data):
		self.data = data
		self.length = 0

	def eat(self, leng = 1):
		begin = self.length
		self.length += leng
		if self.length < len(self.data):
			return self.data[begin:self.length]
		return None

	def throw(self, msg = ''):
		raise Exception(msg)

	def readNum(self):
		ret = ''
		char = self.data[self.length]
		while char.isdigit() and self.length < len(self.data):
			ret += char
			self.length += 1
			char = self.data[self.length]
		if char == '.':
			ret += char
			self.length += 1
			char = self.data[self.length]
			
			while char.isdigit() and self.length < len(self.data):
				ret += char
				self.length += 1
				char = self.data[self.length]

			return float(ret)

		return int(ret)

	def next(self):
		char = self.data[self.length]
		if char == 's':
			return self.string()
		if char == 'i':
			return self.integer()
		if char == 'd':
			return self.double()
		if char == 'b':
			return self.boolean()
		if char == 'N':
			return self.null()
		if char == 'a':
			return self.array()
		if char == 'O':
			return self.object()

		self.throw('undefined type')

	def string(self):
		self.eat() # eat s
		self.eat() # eat :
		len = self.readNum()
		self.eat() # eat :
		self.eat() # eat "
		value = self.eat(len)
		self.eat() # eat "
		self.eat() # eat ;
		return Token("string", value)

	def integer(self):
		self.eat() # eat i
		self.eat() # eat :
		value = self.readNum()
		self.eat() # eat ;
		return Token("integer", value)

	def double(self):
		self.eat() # eat d
		self.eat() # eat :
		value = self.readNum()
		self.eat() # eat ;
		return Token("double", value)

	def boolean(self):
		self.eat() # eat b
		self.eat() # eat :
		value = self.readNum()
		if value == 0:
			value = False
		else:
			value = True
		self.eat() # eat ;
		return Token("boolean", value)

	def null(self):
		self.eat() # eat N
		self.eat() # eat ;
		return Token("null")

	def array(self):
		self.eat() # eat a
		self.eat() # eat :
		size = self.readNum()
		self.eat() # eat :
		self.eat() # eat {
		ret = {}
		for i in range(0, size):
			key = self.next()
			value = self.next()
			ret[key.value] = value
		self.eat() # eat }
		return Token("array", ret)

	def object(self):
		self.eat() # eat o
		self.eat() # eat :
		size = self.readNum()
		self.eat() # eat :
		self.eat() # eat "
		clsname = self.eat(size)
		self.eat() # eat "
		self.eat() # eat :
		objsize = self.readNum()
		self.eat() # eat :
		self.eat() # eat {
		ret = {}

		for i in range(0, objsize):
			key = self.next()
			value = self.next()
			ret[key.value] = value
		self.eat() # eat }

		return Token("obj:%s" % clsname, ret)

	def visit(self, token):
		if token.type in ("string", "integer", "double", "boolean", "null"):
			return token.value

		ret = {}
		for i in token.value:
			ret[i] = self.visit(token.value[i])

		return ret

	def parse(self):
		token = self.next()
		return self.visit(token)