"""add click column into table Article

Revision ID: 864a162aca7d
Revises: None
Create Date: 2017-05-24 15:45:43.446015

"""

# revision identifiers, used by Alembic.
revision = '864a162aca7d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Article', sa.Column('click', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Article', 'click')
    # ### end Alembic commands ###
