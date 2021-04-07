
CXX = g++
CXXFLAGS = -Wall -g
LIBS = -lglfw -lGLU -lGL -lX11 -lXxf86vm -lXrandr -lpthread -lXi
DEPENDENCIES = main.o #error.o sWindow.o

test: $(DEPENDENCIES)
	$(CXX) $(CXXFLAGS) -o test-bin $(DEPENDENCIES) $(LIBS)

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp $(LIBS)

clean:
	rm -f *.o main
	echo "Clean done"
