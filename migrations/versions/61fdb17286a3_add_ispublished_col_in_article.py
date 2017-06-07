"""add isPublished col in Article

Revision ID: 61fdb17286a3
Revises: 70e98d52e507
Create Date: 2017-06-07 10:45:32.093965

"""

# revision identifiers, used by Alembic.
revision = '61fdb17286a3'
down_revision = '70e98d52e507'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Article', sa.Column('isPublished', sa.Boolean(), nullable=True))
    # op.create_index(op.f('ix_User_name'), 'User', ['name'], unique=True)
    # op.drop_index('ix_User_name', table_name='User')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_index('ix_User_name', 'User', ['name'], unique=True)
    # op.drop_index(op.f('ix_User_name'), table_name='User')
    op.drop_column('Article', 'isPublished')
    # ### end Alembic commands ###
