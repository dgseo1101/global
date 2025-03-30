"""attempt_seed

Revision ID: 6be09d6dc59c
Revises: a6a79f4613de
Create Date: 2025-03-30 17:22:08.036183+09:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6be09d6dc59c'
down_revision: Union[str, None] = 'a6a79f4613de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attempt_seed',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('quiz_attempt_id', sa.Integer(), nullable=False),
    sa.Column('seed', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quiz_attempt_id'], ['quiz_attempt.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('quiz_attempt_question_choice')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz_attempt_question_choice',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('attempt_question_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('choice_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('choice_order', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['attempt_question_id'], ['quiz_attempt_question.id'], name='quiz_attempt_question_choice_attempt_question_id_fkey'),
    sa.ForeignKeyConstraint(['choice_id'], ['choice.id'], name='quiz_attempt_question_choice_choice_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='quiz_attempt_question_choice_pkey')
    )
    op.drop_table('attempt_seed')
    # ### end Alembic commands ###
