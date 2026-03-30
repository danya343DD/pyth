#ifndef VARIANT1_3_H
#define VARIANT1_3_H

#include <QMainWindow>
#include <QString>
#include <QMessageBox>

QT_BEGIN_NAMESPACE
namespace Ui { class variant1_3; }
QT_END_NAMESPACE

class variant1_3 : public QMainWindow
{
    Q_OBJECT

public:
    variant1_3(QWidget *parent = nullptr);
    ~variant1_3();

private slots:
    void on_pushButton1_clicked();  // Слот для первой задачи
    void on_pushButton2_clicked();  // Слот для второй задачи

private:
    Ui::variant1_3 *ui;
};

#endif // VARIANT1_3_H