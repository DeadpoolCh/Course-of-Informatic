"""
- __init__() -  инициализация экземпляра класса. Конструирует новый объект типа Vector3D
                из трех чисел с плавающей точкой(float). По умолчанию конструирует нулевой вектор.
                Если пользователь попытается инициализировать объект нечисловыми типами,
                необходимо бросить исключение;
- __repr__() -  возвращает текстовую строку: `'Vector3D(x, y, z)'`, где x, y, z - значения компонент;
- __abs__() -   возвращает длину вектора;
- __bool__() -  возвращает True, если вектор ненулевой, иначе - False;
- __eq__(other) - сравнивает два вектора, возвращает True, если векторы равны покомпонентно, иначе False;
- __neg__() -   возвращает новый объект типа Vector3D, компоненты которого равны компонентам данного вектора,
                домноженным на минус единицу;
- __add__(other) - складывает два вектора, возвращает новый объект типа Vector3D - сумму;
- __sub__(other) - вычитает вектор other из данного вектора, возвращает новый объект типа Vector3D - разность;
- __mul__(scalar) - умножение вектора на скаляр слева, возвращает новый объект типа Vector3D - произведение;
- __rmul__(scalar) - умножение вектора на скаляр справа, возвращает новый объект типа Vector3D - произведение;
- __truediv__(scalar) - деление вектора на скаляр, возвращает новый объект типа Vector3D - частное;
- dot(other) - возвращает результат скалярного произведения;
- cross(other) - возвращает векторное произведение между векторами;

"""

from typing import Generator, Any


class Vector3D:
	_x: float
	_y: float
	_z: float

	def __init__(self,x: float = 0,y: float = 0,z: float = 0) -> None:
		try:
			self._x=float(x)
			self._y=float(y)
			self._z=float(z)
		except:
			print("Попробуйте ввести координаты снова. Используйте только числа с плавающей точкой")
	def __iter__(self) -> Generator[float, None, None]:
		pass
	def __repr__(self) -> str:
		return f"Vector3D{self._x,self._y,self._z}"
	def __abs__(self) -> float:
		return f"{(self._x**2+self._y**2+self._z**2)**0.5:.2f}"
	def __bool__(self) -> bool:
		koord=[self._x==0,self._y==0,self._z==0]
		if any(koord): return False
		else: return  True
	def __eq__(self, other: Any) -> bool:
		koords=[self._x==other._x,self._y==other._y,self._z==other._z]
		if all(koords): return True
		else: return False
	def __neg__(self):
		return Vector3D(self._x*(-1),self._y*(-1),self._z*(-1))
	def __add__(self, other):
		return Vector3D(self._x+other._x,self._y+other._y,self._z+other._z)
	def __sub__(self, other):
		return Vector3D(self._x-other._x,self._y-other._y,self._z-other._z)
	def __mul__(self, scalar: float):
		return Vector3D(self._x*scalar,self._y*scalar,self._z*scalar)
	def __rmul__(self, scalar: float):
		return Vector3D(scalar*self._x,scalar*self._y,scalar*self._z)
	def __truediv__(self, scalar):
		return Vector3D(self._x/scalar,self._y/scalar,self._z/scalar)
	def dot(self, other) -> float:
		return Vector3D(self._x*other._x,self._y*other._y,self._z*other._z)
	def cross(self, other):
		return Vector3D(self._y*other._z-self._z*other._y,self._x*other._z-self._z*other._x,self._x*other._y-self._y*other._x)

	@property
	def x(self) -> float:
		pass

	@property
	def y(self) -> float:
		pass

	@property
	def z(self) -> float:
		pass

vector= Vector3D(1,2,3)
vector2= Vector3D(3,2,1)
print(vector.__repr__())
print(vector2.__repr__())
print(vector.__abs__())
print(vector.__bool__())
print(vector.__eq__(vector2))
print(vector.__neg__())
print(vector.__add__(vector2))
print(vector.__sub__(vector2))
print(vector.dot(vector2))
print(vector.cross(vector2))


