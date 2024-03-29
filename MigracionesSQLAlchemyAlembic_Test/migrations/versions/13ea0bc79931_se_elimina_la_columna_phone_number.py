"""Se elimina la columna phone_number

Revision ID: 13ea0bc79931
Revises: 49aae57dc631
Create Date: 2023-12-12 15:44:45.250581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13ea0bc79931'
down_revision = '49aae57dc631'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'phone_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
