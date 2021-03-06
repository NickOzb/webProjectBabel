# Generated by Django 3.1.7 on 2021-04-26 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namebanka', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='Dvizhenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolvotovara', models.IntegerField(null=1)),
                ('cena', models.IntegerField(null=1)),
            ],
            options={
                'verbose_name': 'Движение товара',
                'verbose_name_plural': 'Движение товаров',
            },
        ),
        migrations.CreateModel(
            name='Kategoriitovara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namekategorii', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товара',
            },
        ),
        migrations.CreateModel(
            name='Nakladnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('priznak', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Накладная',
                'verbose_name_plural': 'Накладные',
            },
        ),
        migrations.CreateModel(
            name='Nalogi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namenaloga', models.CharField(max_length=20)),
                ('percent', models.IntegerField(null=1)),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
            },
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('edizm', models.CharField(max_length=10)),
                ('kodkategorii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.kategoriitovara')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Taksirovka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sumnaloga', models.IntegerField(null=1)),
                ('kodnaloga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.nalogi')),
                ('nnakladnoy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.dvizhenie')),
            ],
            options={
                'verbose_name': 'Таксировка',
                'verbose_name_plural': 'Таксировки',
            },
        ),
        migrations.CreateModel(
            name='Podrazdeleniya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namesklada', models.CharField(max_length=20)),
                ('fio', models.CharField(max_length=40)),
                ('kodsklada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.nakladnie')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.CreateModel(
            name='Ostatki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srcena', models.IntegerField(null=1)),
                ('kolvotovarananachalo', models.IntegerField(null=1)),
                ('kolvoprihod', models.IntegerField(null=1)),
                ('kolvorashod', models.IntegerField(null=1)),
                ('articul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.tovar')),
            ],
            options={
                'verbose_name': 'Остаток',
                'verbose_name_plural': 'Остатки',
            },
        ),
        migrations.CreateModel(
            name='Organizatsiya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameorg', models.CharField(max_length=20)),
                ('schetorg', models.IntegerField(null=1)),
                ('adress', models.CharField(max_length=40)),
                ('fioruk', models.CharField(max_length=40)),
                ('phone', models.IntegerField(null=1)),
                ('kodbanka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.bank')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.AddField(
            model_name='nakladnie',
            name='kodorg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.organizatsiya'),
        ),
        migrations.AddField(
            model_name='nakladnie',
            name='nnakladnoy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.dvizhenie'),
        ),
        migrations.AddField(
            model_name='dvizhenie',
            name='articul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebProjectApplication.tovar'),
        ),
    ]
