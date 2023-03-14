"""empty message

Revision ID: 41fbb05067ef
Revises: 6e820a019d98
Create Date: 2023-03-14 19:27:21.517960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41fbb05067ef'
down_revision = '6e820a019d98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('professional', schema=None) as batch_op:
        batch_op.drop_column('foto_perfil')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('es_profesional',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.drop_column('telefono')
        batch_op.drop_column('direccion')
        batch_op.drop_column('ciudad')
        batch_op.drop_column('codigo_postal')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('codigo_postal', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('ciudad', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('direccion', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('telefono', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
        batch_op.alter_column('es_profesional',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    with op.batch_alter_table('professional', schema=None) as batch_op:
        batch_op.add_column(sa.Column('foto_perfil', sa.VARCHAR(length=120), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
