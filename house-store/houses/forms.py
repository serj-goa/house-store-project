from django import forms as f


class HousesFilterForm(f.Form):
    min_price = f.IntegerField(label='от', required=False)
    max_price = f.IntegerField(label='до', required=False)

    query = f.CharField(label='Описание', required=False)
    ordering = f.ChoiceField(
        label='Сортировка',
        required=False,
        choices=(
            ('name', 'по алфавиту'),
            ('price', 'сначала дешевые'),
            ('-price', 'сначала дорогие'),
        )
    )
