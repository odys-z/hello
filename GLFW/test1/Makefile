
CXX = g++
CXXFLAGS = -Wall -g
LIBS = -lglfw -lGLU -lGL -lX11 -lXxf86vm -lXrandr -lpthread -lXi
DEPENDENCIES = main.o #error.o sWindow.o

# ****************************************************
# Targets needed to bring the executable up to date

test: $(DEPENDENCIES)
	$(CXX) $(CXXFLAGS) -o test-bin $(DEPENDENCIES) $(LIBS)

main.o: main.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp $(LIBS)

# error.o: error.cpp
# 	$(CXX) $(CXXFLAGS) -c error.cpp $(LIBS)
#
# sWindow.o: sWindow.cpp
# 	$(CXX) $(CXXFLAGS) -c sWindow.cpp $(LIBS)

clean:
	rm -f *.o main
	echo "Clean done"
