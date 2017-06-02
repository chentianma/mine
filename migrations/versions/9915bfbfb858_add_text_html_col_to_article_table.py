"""add text_html col to Article table 

Revision ID: 9915bfbfb858
Revises: 864a162aca7d
Create Date: 2017-05-26 09:28:31.600630

"""

# revision identifiers, used by Alembic.
revision = '9915bfbfb858'
down_revision = '864a162aca7d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Article', sa.Column('text_html', sa.Text(), nullable=True))
    # op.create_index(op.f('ix_User_name'), 'User', ['name'], unique=True)
    # op.drop_index('ix_User_name', table_name='User')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_index('ix_User_name', 'User', ['name'], unique=True)
    # op.drop_index(op.f('ix_User_name'), table_name='User')
    op.drop_column('Article', 'text_html')
    # ### end Alembic commands ###