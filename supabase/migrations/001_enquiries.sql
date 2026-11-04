-- Contact-form enquiries for the personal site.
-- Run this once in the Supabase SQL editor for project kckywwwommpntwcejrzw.
-- Visitors can add an enquiry but can never read, change or delete one.
-- You read them in Supabase under Table Editor → enquiries.

create table if not exists public.enquiries (
  id           uuid primary key default gen_random_uuid(),
  created_at   timestamptz not null default now(),
  audience     text not null,
  topic        text not null,
  name         text not null,
  organisation text,
  email        text not null,
  message      text not null,
  constraint enquiries_lengths check (
    char_length(audience) between 1 and 60
    and char_length(topic) between 1 and 80
    and char_length(name) between 1 and 120
    and (organisation is null or char_length(organisation) <= 160)
    and char_length(email) between 3 and 200
    and email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$'
    and char_length(message) between 1 and 4000
  )
);

alter table public.enquiries enable row level security;

drop policy if exists "Visitors can send an enquiry" on public.enquiries;
create policy "Visitors can send an enquiry"
  on public.enquiries for insert
  to anon
  with check (true);

revoke all on public.enquiries from anon;
grant insert on public.enquiries to anon;
