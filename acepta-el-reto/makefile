CC = g++
EXE = 106

all: clean comp run

clean:
	rm -f a.out

comp:
	@echo "Compiling $(EXE)"
	$(CC) $(CFLAGS) $(EXE)/main.cpp

run :
	@echo "----------------- Running $(EXE) -----------------"
	./a.out < $(EXE)/in

copy:
	@echo "Creating new directory for exercise $(EXE)"
	mkdir $(EXE)
	cp -R base/* $(EXE)/
