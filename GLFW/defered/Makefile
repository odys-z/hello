
CXX = g++
CXXFLAGS = -Wall -g
LIBS = -lglfw -lGLU -lGL -lX11 -lXxf86vm -lXrandr -lpthread -lXi
INC=-I../glad/include -I../glwf-3 -I.. -I../stb
DEPENDENCIES = main.o

test: $(DEPENDENCIES)
	$(CXX) $(CXXFLAGS) -o test-bin $(DEPENDENCIES) $(LIBS)

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp $(INC) $(LIBS)

clean:
	rm -f *.o main
	echo "Clean done"
