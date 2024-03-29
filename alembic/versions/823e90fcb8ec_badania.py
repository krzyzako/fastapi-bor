"""badania

Revision ID: 823e90fcb8ec
Revises: 30cfe63241ce
Create Date: 2022-01-27 13:45:39.050490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '823e90fcb8ec'
down_revision = '30cfe63241ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nr_badania', sa.Column('nr_badania', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_nr_badania_zbiorniki_id_nr_badania', 'nr_badania', 'zbiorniki', ['nr_badania'], ['id'])
    op.drop_constraint('fk_zbiorniki_nr_badania_id_nr_badania', 'zbiorniki', type_='foreignkey')
    op.drop_column('zbiorniki', 'nr_badania')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('zbiorniki', sa.Column('nr_badania', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('fk_zbiorniki_nr_badania_id_nr_badania', 'zbiorniki', 'nr_badania', ['nr_badania'], ['id'])
    op.drop_constraint('fk_nr_badania_zbiorniki_id_nr_badania', 'nr_badania', type_='foreignkey')
    op.drop_column('nr_badania', 'nr_badania')
    # ### end Alembic commands ###
