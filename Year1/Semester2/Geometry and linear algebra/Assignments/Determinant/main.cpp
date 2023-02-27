#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <chrono>
#include <fstream>

#define M 101
// Function to print the matrix
void PrintMatrix(float a[][M], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            std::cout << a[i][j] << " ";
        std::cout << std::endl;
    }
}

void GaussMethod(float a[][M], int n)
{
    int i, j, k = 0, c, m = 0;
    float pro = 0;

    // Performing elementary operations
    for (i = 0; i < n; i++)
    {
        if (a[i][i] == 0)
        {
            c = 1;
            while ((i + c) < n && a[i + c][i] == 0)
                c++;
            for (j = i, k = 0; k < n; k++)
                std::swap(a[j][k], a[j + c][k]);
        }

        for (j = 0; j < n; j++)
        {

            // Excluding all i == j
            if (i != j)
            {

                // Converting Matrix to reduced row
                // echelon form(diagonal matrix)
                float pro = a[j][i] / a[i][i];

                for (k = 0; k < n; k++)
                    a[j][k] = a[j][k] - (a[i][k]) * pro;
            }
        }
    }
    int result = 1;
    std::cout << "Result is : ";
    for (int i = 0; i < n; i++)
        result *= a[i][i];
    std::cout << result << std::endl;
}
int NormalMethod(float a[][M], int n)
{
    int det = 0, p, h, k, i, j;
    float temp[M][M];
    if (n == 1)
        return a[0][0];
    else if (n == 2)
    {
        det = (a[0][0] * a[1][1] - a[0][1] * a[1][0]);
        return det;
    }
    else
    {
        for (p = 0; p < n; p++)
        {
            h = 0;
            k = 0;
            for (i = 1; i < n; i++)
            {
                for (j = 0; j < n; j++)
                {
                    if (j == p)
                    {
                        continue;
                    }
                    temp[h][k] = a[i][j];
                    k++;
                    if (k == n - 1)
                    {
                        h++;
                        k = 0;
                    }
                }
            }
            det = det + a[0][p] * pow(-1, p) * NormalMethod(temp, n - 1);
        }
        return det;
    }
}
int main()
{
    int n = 2;
    float matrix1[101][101], matrix2[101][101],sum_gauss=0,sum_normal=0;
    srand(time(0));
    std::ofstream MyFile("time.txt");
    int cnt=0;
    while (n <= 10)
    {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                matrix1[i][j] = 1 + rand() % 100;
                matrix2[i][j] = matrix1[i][j];
            }
        std::cout << "Initial Matrix is :" << std::endl;
        PrintMatrix(matrix1, n);
        std::cout << std::endl;
        std::cout << "Gauss Method result :" << std::endl;
        auto begin1 = std::chrono::high_resolution_clock::now();
        GaussMethod(matrix1, n);
        auto end1 = std::chrono::high_resolution_clock::now();
        auto elapsed_gauss = std::chrono::duration_cast<std::chrono::microseconds>(end1 - begin1);
        std::cout << std::endl;
        std::cout << "Normal Method result :" << std::endl;
        auto begin2 = std::chrono::high_resolution_clock::now();
        std::cout << NormalMethod(matrix2, n) << std::endl;
        auto end2 = std::chrono::high_resolution_clock::now();
        auto elapsed_normal = std::chrono::duration_cast<std::chrono::microseconds>(end2 - begin2);
        cnt++;
        sum_gauss+=elapsed_gauss.count();
        sum_normal+=elapsed_normal.count();
        if(cnt==100)
        {
            MyFile <<n<<";"<<sum_gauss/100 <<";"<<sum_normal/100<< std::endl;
            n++;
            cnt=0;
            sum_gauss=sum_normal=0;
        }
    }
    MyFile.close();
    return 0;
}