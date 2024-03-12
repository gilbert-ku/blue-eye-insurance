"""add medical model

Revision ID: 784cc7923465
Revises: 91e111ca28c8
Create Date: 2024-03-12 22:33:09.659760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '784cc7923465'
down_revision = '91e111ca28c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medical',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('cover_type', sa.String(length=100), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('meeting', sa.String(length=100), nullable=False),
    sa.Column('app_date', sa.Date(), nullable=False),
    sa.Column('app_time', sa.String(), nullable=False),
    sa.Column('comment', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medical')
    # ### end Alembic commands ###