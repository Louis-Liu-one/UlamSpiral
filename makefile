
NAME = eratothenes

pack: $(NAME).c setup.py
	python3 setup.py install
	mv build/lib.macosx-10.13-universal2-cpython-313/$(NAME).cpython-313-darwin.so .
	rm -r build dist $(NAME).egg-info

run:
	python3 UlamSpiralCreator.py
	open UlamSpiral.png
