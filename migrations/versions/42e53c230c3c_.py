"""empty message

Revision ID: 42e53c230c3c
Revises: 45a4e74cdaa9
Create Date: 2023-03-12 03:01:18.790308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42e53c230c3c'
down_revision = '45a4e74cdaa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'professional', ['professional_user'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'professional', type_='unique')
    # ### end Alembic commands ###
