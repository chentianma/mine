"""add category_id foreignkey in Topic

Revision ID: 0b6f90cadb82
Revises: a06c8b2e1c5e
Create Date: 2017-05-27 13:52:21.541292

"""

# revision identifiers, used by Alembic.
revision = '0b6f90cadb82'
down_revision = 'a06c8b2e1c5e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Topic', sa.Column('category_id', sa.Integer(), nullable=True))
    op.alter_column('Topic', 'title',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=100),
               nullable=True)
    op.create_foreign_key(None, 'Topic', 'Category', ['category_id'], ['id'])
    # op.create_index(op.f('ix_User_name'), 'User', ['name'], unique=True)
    # op.drop_index('ix_User_name', table_name='User')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_index('ix_User_name', 'User', ['name'], unique=True)
    # op.drop_index(op.f('ix_User_name'), table_name='User')
    op.drop_constraint(None, 'Topic', type_='foreignkey')
    op.alter_column('Topic', 'title',
               existing_type=mysql.VARCHAR(collation='utf8_bin', length=100),
               nullable=False)
    op.drop_column('Topic', 'category_id')
    # ### end Alembic commands ###
