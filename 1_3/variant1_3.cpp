#include "variant1_3.h"
#include "ui_variant1_3.h"
#include <QDebug>
#include <QMessageBox>
#include <QString>

variant1_3::variant1_3(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::variant1_3)
{
    ui->setupUi(this);
}

variant1_3::~variant1_3()
{
    delete ui;
}

// ============================================
// ПЕРВАЯ ЗАДАЧА: Заменить наибольшее из трех чисел разностью двух других
// ============================================
void variant1_3::on_pushButton1_clicked()
{
    // Получаем текст из полей ввода
    QString str1 = ui->lineEdit1->text();
    QString str2 = ui->lineEdit2->text();
    QString str3 = ui->lineEdit3->text();

    // Преобразуем в числа
    bool ok1, ok2, ok3;
    float num1 = str1.toFloat(&ok1);
    float num2 = str2.toFloat(&ok2);
    float num3 = str3.toFloat(&ok3);

    // Проверка на корректность ввода
    if(!ok1 || !ok2 || !ok3) {
        QMessageBox::information(this, "Ошибка", "Введите числа!");
        return;
    }

    // Находим наибольшее и заменяем его разностью двух других
    float result;

    if(num1 >= num2 && num1 >= num3) {
        // num1 - наибольшее, заменяем на (num2 - num3)
        result = num2 - num3;
        ui->labelResult1->setText(QString("Наибольшее число %1 заменено на разность: %2 - %3 = %4")
                                      .arg(num1).arg(num2).arg(num3).arg(result));
    }
    else if(num2 >= num1 && num2 >= num3) {
        // num2 - наибольшее, заменяем на (num1 - num3)
        result = num1 - num3;
        ui->labelResult1->setText(QString("Наибольшее число %1 заменено на разность: %2 - %3 = %4")
                                      .arg(num2).arg(num1).arg(num3).arg(result));
    }
    else {
        // num3 - наибольшее, заменяем на (num1 - num2)
        result = num1 - num2;
        ui->labelResult1->setText(QString("Наибольшее число %1 заменено на разность: %2 - %3 = %4")
                                      .arg(num3).arg(num1).arg(num2).arg(result));
    }
}

// ============================================
// ВТОРАЯ ЗАДАЧА: Работа с переменными A и B
// ============================================
void variant1_3::on_pushButton2_clicked()
{
    // Получаем текст из полей ввода
    QString strA = ui->lineEditA->text();
    QString strB = ui->lineEditB->text();

    // Преобразуем в целые числа
    bool okA, okB;
    int A = strA.toInt(&okA);
    int B = strB.toInt(&okB);

    // Проверка на корректность ввода
    if(!okA || !okB) {
        QMessageBox::information(this, "Ошибка", "Введите целые числа!");
        return;
    }

    // Обрабатываем согласно условию
    if(A != B) {
        // Если не равны - присваиваем максимум обеим
        int maxVal = (A > B) ? A : B;
        A = maxVal;
        B = maxVal;
        ui->labelResult2->setText(QString("A и B не равны.\nОбеим переменным присвоен максимум: A = %1, B = %2").arg(A).arg(B));
    }
    else {
        // Если равны - присваиваем нули
        A = 0;
        B = 0;
        ui->labelResult2->setText(QString("A и B равны.\nОбеим переменным присвоен 0: A = %1, B = %2").arg(A).arg(B));
    }
}