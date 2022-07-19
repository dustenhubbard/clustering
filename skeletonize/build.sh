F=skeletonize

g++ -std=c++14 -O3 -g $F.cpp -o $F  -I../CGAL-5.0.2/include -I../eigen-3.3.7 -DCGAL_EIGEN3_ENABLED -lgmp -lmpfr
