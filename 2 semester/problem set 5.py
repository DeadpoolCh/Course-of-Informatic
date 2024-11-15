# def geom_progresive(start:int,step:int):
# 	yield start
# 	while True:
# 		iters=start*step
# 		yield iters
# 		start=iters
#
# gen=geom_progresive(2,2)
# for _ in range(50):
# 	print(next(gen))


def wheel(time_limit: int, pause: int):
	""" Отрисовка спиннера.

		Печатает на экран надпись: 'Thinking: <symbol>',
		где вместо <symbol> последовательно появляются знаки: \\, \\|, /, -,
		что создаёт эффект вращения.

		Вход:
			time_limit: float
				время (в секундах), в течение которого должна производиться отрисовка спиннера
			pause: float
				время (в милисекундах) задержки между сменой символов спиннера

		Выход:
			None
	"""
	elapsed_time=0
	wheels=r'\|/-'
	print('Thinking: ',end='')
	while True:
		if elapsed_time>=time_limit:
			break
		for i in range(time_limit*len(wheels)):
			print(wheels[i%len(wheels)], end='')
			for _ in range(pause*10**7):
				pass
			print('\b', end='', flush=True)
		elapsed_time+=1


wheel(50**3,2)









































