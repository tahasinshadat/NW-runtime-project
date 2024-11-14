#include <iostream>
#include <chrono>

void n1(int n) {
    for (int i = 0; i < n; ++i) {
        std::cout << "n1 : print " << n << std::endl;
    }
}

void n2(int n) {
    int count = 1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout << "n2 : print " << count << std::endl;
            ++count;
        }
    }
}

void n3(int n) {
    int count = 1;
    for (int a = 0; a < n; ++a) {
        for (int b = 0; b < n; ++b) {
            for (int c = 0; c < n; ++c) {
                std::cout << "n3 : print " << count << std::endl;
                ++count;
            }
        }
    }
}

void n4(int n) {
    int count = 1;
    for (int a = 0; a < n; ++a) {
        for (int b = 0; b < n; ++b) {
            for (int c = 0; c < n; ++c) {
                for (int d = 0; d < n; ++d) {
                    std::cout << "n4 : print " << count << std::endl;
                    ++count;
                }
            }
        }
    }
}

void n5(int n) {
    int count = 1;
    for (int a = 0; a < n; ++a) {
        for (int b = 0; b < n; ++b) {
            for (int c = 0; c < n; ++c) {
                for (int d = 0; d < n; ++d) {
                    for (int e = 0; e < n; ++e) {
                        std::cout << "n5 : print " << count << std::endl;
                        ++count;
                    }
                }
            }
        }
    }
}

void timeAndRun(void (*func)(int), int n, int iterations) {
    auto start = std::chrono::high_resolution_clock::now(); // Start the timer

    for (int i = 0; i < iterations; ++i) {
        func(n);
    }

    auto end = std::chrono::high_resolution_clock::now(); // End the timer
    std::cout << "\033[2J\033[1;1H"; // Clear console
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Time taken to run " << iterations << " iteration(s): "
              << elapsed.count() << " seconds" << std::endl;
}

int main() {
    timeAndRun(n3, 10, 10);
    return 0;
}
