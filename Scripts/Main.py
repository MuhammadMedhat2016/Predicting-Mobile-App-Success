import Scripts.PreprocessLib as Pre
import Scripts.Regression as Reg
import numpy as np
import pickle


if __name__ == '__main__':
    w = tf.Variable(0, dtype= tf.float32)

    '''
    data = Pre.run()

    data = data.astype(np.float64)
    #data = np.delete(data, 9, axis=1)
    res = Reg.multi_variant_regression(data)

    print(f'Multiple Linear Model R-Squared, SSE, MSE {res[0]:.3f} {res[1]:.3f} {res[2]:.3f}')
    filename = 'multivar.sav'
    pickle.dump(res[3], open(filename, 'wb'))
    with open('observations1.txt', 'w') as file:
        j = 0
        for ele1, ele2 in zip(res[4], res[5]):
            file.write(f"{j}, {ele1:.5f},  {ele2:.5f}, {(ele1 - ele2):.5f}, {(ele1 - ele2) ** 2:.5f}")
            file.write('\n')
            j += 1
    for i in range(2, 5):
        res = Reg.polynomial_regression(data, i)
        print(f'Polynomial Linear Model of degree {i} R-Squared, SSE, MSE {res[0]:.3f} {res[1]:.3f} {res[2]:.3f}')
        filename = f'deg{i}poly.sav'
        pickle.dump(res[3], open(filename, 'wb'))
        with open(f'observations{i}.txt', 'w') as file:
            j = 0
            for ele1, ele2 in zip(res[4], res[5]):
                file.write(f"{j}, {ele1:.5f},  {ele2:.5f}, {(ele1 - ele2):.5f}, {(ele1 - ele2) ** 2:.5f}")
                file.write('\n')
                j += 1
'''