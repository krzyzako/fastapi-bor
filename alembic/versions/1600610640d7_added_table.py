"""Added table

Revision ID: 1600610640d7
Revises: 
Create Date: 2022-01-21 08:15:21.061811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1600610640d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_usersbase_admin', table_name='usersbase')
    op.drop_index('ix_usersbase_email', table_name='usersbase')
    op.drop_index('ix_usersbase_first_name', table_name='usersbase')
    op.drop_index('ix_usersbase_id', table_name='usersbase')
    op.drop_index('ix_usersbase_last_name', table_name='usersbase')
    op.drop_table('usersbase')
    op.drop_index('ix_hero_age', table_name='hero')
    op.drop_index('ix_hero_id', table_name='hero')
    op.drop_index('ix_hero_name', table_name='hero')
    op.drop_index('ix_hero_secret_name', table_name='hero')
    op.drop_table('hero')
    op.drop_table('users')
    op.add_column('homolog', sa.Column('rodzaj', sa.Integer(), nullable=True))
    op.drop_constraint('fk_homolog_rodzaje_id_rodzaje', 'homolog', type_='foreignkey')
    op.create_foreign_key('fk_homolog_rodzaje_id_rodzaj', 'homolog', 'rodzaje', ['rodzaj'], ['id'])
    op.drop_column('homolog', 'rodzaje')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('homolog', sa.Column('rodzaje', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint('fk_homolog_rodzaje_id_rodzaj', 'homolog', type_='foreignkey')
    op.create_foreign_key('fk_homolog_rodzaje_id_rodzaje', 'homolog', 'rodzaje', ['rodzaje'], ['id'])
    op.drop_column('homolog', 'rodzaj')
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(length=15), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('confirmation', sa.CHAR(length=32), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('username', name='users_username_key')
    )
    op.create_table('hero',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('secret_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='hero_pkey')
    )
    op.create_index('ix_hero_secret_name', 'hero', ['secret_name'], unique=False)
    op.create_index('ix_hero_name', 'hero', ['name'], unique=False)
    op.create_index('ix_hero_id', 'hero', ['id'], unique=False)
    op.create_index('ix_hero_age', 'hero', ['age'], unique=False)
    op.create_table('usersbase',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='usersbase_pkey'),
    sa.UniqueConstraint('name', name='usersbase_name_key')
    )
    op.create_index('ix_usersbase_last_name', 'usersbase', ['last_name'], unique=False)
    op.create_index('ix_usersbase_id', 'usersbase', ['id'], unique=False)
    op.create_index('ix_usersbase_first_name', 'usersbase', ['first_name'], unique=False)
    op.create_index('ix_usersbase_email', 'usersbase', ['email'], unique=False)
    op.create_index('ix_usersbase_admin', 'usersbase', ['admin'], unique=False)
    # ### end Alembic commands ###
