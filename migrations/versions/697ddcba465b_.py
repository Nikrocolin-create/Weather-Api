"""empty message

Revision ID: 697ddcba465b
Revises: 0fc92481402f
Create Date: 2020-08-12 16:08:04.242913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '697ddcba465b'
down_revision = '0fc92481402f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_requests', sa.Column('windspeed', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_requests', 'windspeed')
    # ### end Alembic commands ###
